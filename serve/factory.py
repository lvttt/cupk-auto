from flask import Flask
from flask_cors import CORS
from blueprints.jwxt import jwxt_bp
from blueprints.rhmh import rhmh_bp
from settings import UserConfig, jwxtUrlConfig, SessionConfig, courseDataConfig, rhmhUrlConfig

def create_app():
    app = Flask(__name__)
    # 加载配置类
    app.config.from_object(UserConfig)
    app.config.from_object(jwxtUrlConfig)
    app.config.from_object(rhmhUrlConfig)
    app.config.from_object(SessionConfig)
    app.config.from_object(courseDataConfig)
    # 注册蓝图
    app.register_blueprint(jwxt_bp, url_prefix='/jwxt')
    app.register_blueprint(rhmh_bp, url_prefix='/rhmh')
    CORS(app)
    return app

