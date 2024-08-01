from fastapi import FastAPI

app = FastAPI(
    title='Web',
    description='developer -> danKo',
    version='0.0.1',
)


@app.get('/')
async def main_page():
    return {'data': 'something'}
