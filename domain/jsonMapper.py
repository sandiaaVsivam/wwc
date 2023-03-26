def to_api_data(instance):
    if isinstance(instance, dict):
        return {to_api_data(k): to_api_data(v) for k, v in instance.items()}
    elif hasattr(instance, '__dict__'):
        data = {}
        for key, value in instance.__dict__.items():
            if key.startswith('_'):
                key = key[1:] # Strip leading underscore
            data[to_api_data(key)] = to_api_data(value)
        return data
    elif isinstance(instance, (list, tuple)):
        return [to_api_data(item) for item in instance]
    else:
        return instance
