from __future__ import absolute_import

class CollectionUtil:
    @classmethod
    def generate_batches(cls, collection, batch_size):
        start_index = 0
        end_index = len(collection)-1
        while (True):
            if start_index > end_index:
                break
            elif start_index + batch_size <= end_index+1:
                # Reads batchsize number of elements starting at start
                yield collection[start_index:start_index+batch_size]
            else:
                # Reads remaining number of elements from start to end
                yield collection[start_index:end_index+1]

            start_index += batch_size