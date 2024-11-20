# repo2/utils.py
def fetch_and_transform(data: str) -> str:
    # 외부에서 데이터를 가져오는 대신 repo1의 결과를 사용
    response = f"Processed: {data}"  # Stub for integration test
    return f"Final Output: {response}"
