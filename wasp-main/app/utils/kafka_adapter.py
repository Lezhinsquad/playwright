##
# kafka_adapter.py 데이터를 Kafka 토픽으로 전송하는 유틸리티 모듈입니다.
##
import os
import re
from urllib.parse import urlparse
import httpx
import logging
from app.utils.singleton_meta import SingletonMeta

logging.basicConfig(level=logging.INFO)


class KafkaAdapter(metaclass=SingletonMeta):
    def __init__(self):
        self.kafka_url = os.getenv(
            "KAFKA_MONITORING_URL",
            "https://msg-bk-dev.lezhin.net/kafka/x-api-log/xapi-lezhin-page-monitoring",
        )
        logging.info(f"Kafka URL: {self.kafka_url}")

    async def send(
        self, result: dict, actor: str = "Page Load Bot", verb: str = "measured"
    ):
        actor = actor
        verb = verb
        parse_url = urlparse(result["url"])
        login_type = (
            result["login_type"] if result["login_type"] == "email" else "social"
        )
        social_type = result["login_type"] if result["login_type"] != "email" else None

        base_url = f"{parse_url.scheme}://{parse_url.netloc}"
        domain_name = (
            re.search(
                r"(?:www\.)?([a-zA-Z0-9-]+)\.[a-zA-Z]{2,6}(\.[a-zA-Z]{2,6})?$",
                parse_url.netloc,
            ).group(1)
            if parse_url.netloc
            else None
        )

        payload = {
            "actor": actor,
            "verb": verb,
            "objectId": result["url"],
            "definitionName": result["title"],
            "success": result["status"] == 200,
            "response": result["status"],
            "extensions": {
                "project": "wasp",
                "service": domain_name,
                "targetURL": base_url,
                "duration": (
                    round(result["load_time"], 2) if result["load_time"] else None
                ),
                "loginType": login_type,
                "socialType": social_type,
            },
        }

        async with httpx.AsyncClient(timeout=10.0, verify=False) as client:
            try:
                response = await client.post(self.kafka_url, json=payload)
                response.raise_for_status()
            except httpx.HTTPStatusError as e:
                print(f"Failed to send Kafka data: {e.response.text}")
            except httpx.RequestError as e:
                print(f"HTTP request failed: {e}")
