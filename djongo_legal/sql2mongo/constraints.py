from djongo_legal.exceptions import NotSupportedError, djongo_access_url

# from djongo_legal import djongo_access_url

print(f'This version of djongo does not support constraints. Visit {djongo_access_url}')
raise NotSupportedError('constraints')
