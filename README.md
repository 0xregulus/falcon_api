Usage
=====

Create an user
- Request
```shell
curl -XPOST http://localhost:5000/v1/users -H "Content-Type: application/json" -d '{
 "username": "test1",
 "email": "test1@gmail.com",
 "password": "test1234"
}'
```

- Response
```json
{
  "meta": {
    "code": 200,
    "message": "OK",
  },
  "data": null
}
```

Log in with email and password

- Request
```shell
curl -XGET http://localhost:5000/v1/users/self/login -H "Content-Type: application/json" -d '{
 "email": "test1@gmail.com",
 "password": "test1234"
}'
```

- Response
```json
{
  "meta": {
    "code": 200,
    "message": "OK"
  },
  "data": {
    "username": "test1",
    "token": "gAAAAABV-TpG0Gk6LhU5437VmJwZwgkyDG9Jj-UMtRZ-EtnuDOkb5sc0LPLeHNBL4FLsIkTsi91rdMjDYVKRQ8OWJuHNsb5rKw==",
    "email": "test1@gmail.com",
    "created": 1442396742,
    "sid": "3595073989",
    "modified": 1442396742,
    "key": "SN7I2X53JC6USSKTNTLFXDJVYQTLQDJP",
    "iv": "QEITTNOEJUXXGBIAJFJO4B4KF4======"
  }
}
```

Check the validation of requested data

- Requset
```shell
curl -XPOST http://localhost:5000/v1/users -H "Content-Type: application/json" -d '{
 "username": "t",
 "email": "test1@gmail.c",
 "password": "123"
}'
```

- Response
```json
{
  "meta": {
    "code": 88,
    "message": "Invalid Parameter",
    "description": {
      "username": "min length is 4",
      "email": "value does not match regex '[a-zA-Z0-9._-]+@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,4}'",
      "password": [
        "value does not match regex '[0-9a-zA-Z]\\w{3,14}'",
        "min length is 8"
      ]
    }
  }
}
```

Get database rollback error in response for duplicated data

- Request
```shell
curl -XPOST http://localhost:5000/v1/users -H "Content-Type: application/json" -d '{
 "username": "test1",
 "email": "test1@gmail.com",
 "password": "test1234"
}'
```

- Response
```json
{
  "meta": {
    "code": 77,
    "message": "Database Rollback Error",
    "description": {
      "details": "(psycopg2.IntegrityError) duplicate key value violates unique constraint \"user_email_key\"\nDETAIL:  Key (email)=(test1@gmail.com) already exists.\n",
      "params": "{'username': 'test1', 'token': 'gAAAAABV-UCq_DneJyz4DTuE6Fuw68JU7BN6fLdxHHIlu42R99sjWFFonrw3eZx7nr7ioIFSa7Akk1nWgGNmY3myJzqqbpOsJw==', 'sid': '6716985526', 'email': 'test1@gmail.com', 'password': '$2a$12$KNlGvL1CP..6VNjqQ0pcjukj/fC88sc1Zpzi0uphIUlG5MjyAp2fS'}"
    }
  }
}
```

Get a collection of users with auth token

- Request
```shell
curl -XGET http://localhost:5000/v1/users/1 -H "Authorization: gAAAAABZxDm8QL_08uTAT1KwoAlMJ0mXhRwD1rLpfXmUYuG5OPiBNtKQ5Z79FyOlUJbXiz4-hf4U8EAr2FoqRG0JyM4VcqhiXg=="
```

- Response
```json
{
  "meta": {
    "code": 200,
    "message": "OK"
  },
  "data": [
    {
      "username": "test1",
      "token": "gAAAAABV-UCAgRy-ee6t4YOLMW84tKr_eOiwgJO0QcAHL7yIxkf1fiMZfELkmJAPWnldptb3iQVzoZ2qJC6YlSioVDEUlLhG7w==",
      "sid": "2593953362",
      "modified": 1442398336,
      "email": "test1@gmail.com",
      "created": 1442398336
    },
    {
      "username": "test2",
      "token": "gAAAAABV-UCObi3qxcpb1XLV4GnCZKqt-5lDXX0YAOcME5bndZjjyzQWFRZKV1x54EzaY2-g5Bt47EE9-45UUooeiBM8QrpSjA==",
      "sid": "6952584295",
      "modified": 1442398350,
      "email": "test2@gmail.com",
      "created": 1442398350
    },
    {
      "username": "test3",
      "token": "gAAAAABV-UCccDCKuG28DbJrObEPUMV5eE-0sEg4jn57usBmIADJvkf3r5gP5F9rX5tSzcBhuBkDJwEJ1mIifEgnp5sxc3Z-pg==",
      "sid": "8972728004",
      "modified": 1442398364,
      "email": "test3@gmail.com",
      "created": 1442398364
    }
  ]
}
```
