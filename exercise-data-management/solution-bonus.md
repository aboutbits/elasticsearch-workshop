Create the policy, that deletes an index that is older than 1 hour.

```
PUT _ilm/policy/logs-cleanup-policy
{
  "policy": {
    "phases": {
      "delete": {
        "min_age": "1h",
        "actions": {
          "delete": {}
        }
      }
    }
  }
}
```

Assign the policy to all indices that match `logs-`.

```
PUT logs-*/_settings 
{
  "index": {
    "lifecycle": {
      "name": "logs-cleanup-policy"
    }
  }
}
```

Elasticsearch will now automatically remove indices that start with `logs-` and have been created more than an 1 hour ago.
