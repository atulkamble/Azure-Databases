import os
import redis


def main():
    host = os.getenv("REDIS_HOST", "redis-demo.redis.cache.windows.net")
    port = int(os.getenv("REDIS_PORT", "6380"))
    password = os.getenv("REDIS_PASSWORD", "ChangeMe123!")

    r = redis.StrictRedis(host=host, port=port, password=password, ssl=True)
    r.setex("session:user123", 60, "active")
    print(r.get("session:user123"))


if __name__ == "__main__":
    main()
