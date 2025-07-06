from aiohttp import web

routes = web.RouteTableDef()

async def omg_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Start !!!")
