from aiohttp import web
import os
import argparse
import http


PATH = os.path.abspath(os.path.curdir)


def create_parser():
    parser = argparse.ArgumentParser(description='Set PORT for async server.')
    parser.add_argument('port', type=int, default=8080, help='PORT number for server')
    return parser

async def handle(request):
    file_name = request.match_info.get('file_name', "None")
    try:
        with open("{}/{}".format(PATH, file_name), 'r') as file:
            return web.Response(text=file.read())
    except FileNotFoundError:
        return web.HTTPInternalServerError()


app = web.Application()
app.router.add_get('/get/{file_name}', handle)

parser = create_parser()
args = parser.parse_args()

web.run_app(app, port=args.port)
