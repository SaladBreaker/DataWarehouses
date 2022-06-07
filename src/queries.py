from src.connection import setup_connection
from src.models import Asset, Source, Data


# https://docs.datastax.com/en/drivers/python/2.5/cqlengine/queryset.html#retrieving-objects-with-filters
def run_query_example():
    setup_connection()

    print("Assets:")
    for asset in Asset.objects().all():
        print(asset)

    print("Sources:")
    for source in Source.objects().all():
        print(source)

    print("Data:")
    for data in Data.objects().all():
        print(data)

    print(f"There are {Asset.objects.count()} data obj entries")

    q = Asset.objects.filter(name='GM')
    print(f"The asset with the name GM is {q.get()}")
