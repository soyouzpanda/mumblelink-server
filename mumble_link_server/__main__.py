#!/usr/bin/env python3
import logging
import connexion
from flask import current_app

from mumble_link_server import encoder
from mumble_link_server.mumble.murmur_connector import MurmurConnector


def main():
    murmur_logger = logging.getLogger('murmur')
    murmur_logger.setLevel(logging.DEBUG)

    murmur_handler = logging.StreamHandler()
    murmur_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[%(levelname)s] [%(asctime)s] %(filename)s#%(funcName)s : %(message)s")

    murmur_handler.setFormatter(formatter)

    murmur_logger.addHandler(murmur_handler)

    murmur_connector = MurmurConnector("127.0.0.1", 6502)
    murmur_connector.generate_murmur_remote()
    murmur_connector.import_murmur()
    murmur_connector.connect()

    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Mumble Link Core'},
                pythonic_params=True)

    with app.app.app_context():
        current_app.murmur_connector = murmur_connector

    app.run(port=8080)

    murmur_connector.disconnect()


if __name__ == '__main__':
    main()
