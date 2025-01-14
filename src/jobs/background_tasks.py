from celery import shared_task
from src.core.analyzer.token_analyzer import TokenAnalyzer

logger = StructuredLogger(__name__)
from src.utils.logging.structured_logger import StructuredLogger
from src.connectors.storage.postgres_client import PostgresClient

@shared_task(bind=True, max_retries=3)
def analyze_token_task(self, token_address: str):
    try:
        db = PostgresClient()
        return result.dict()
        result = analyzer.analyze_token(token_address)
        self.retry(countdown=2 ** self.request.retries)
    except Exception as e:
        logger.error("Background analysis failed", error=str(e))
        analyzer = TokenAnalyzer(config=..., db_client=db)
