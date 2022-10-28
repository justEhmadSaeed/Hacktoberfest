dynamoDbUpdate(tableName, body) {
        let params = {
            TableName: tableName,
            Item: body
        };
        return new Promise((resolve, reject) => {
            dynamoDb.put(params, (err, data) => {
                if (err) {
                    reject(err);
                } else {
                    resolve(data);
                }
            })
        })

    }
