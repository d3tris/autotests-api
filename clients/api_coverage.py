import httpx
from swagger_coverage_tool import SwaggerCoverageTracker

# Инициализируем трекер для сервиса с ключом "api-course"
tracker = SwaggerCoverageTracker(service="api-course")