#list example 

# s3_bucket_list = ["dipendra-bucket-1", "dipendra-bucket-2", "dipendra-bucket-3"]
# print("list of the buskets are:", s3_bucket_list)

#tuple example 

s3_bucket_list = ("dipendra-bucket-1", "dipendra-bucket-2", "dipendra-bucket-3")
print("tuple of the buskets are:", s3_bucket_list)
s3_bucket_list.append("dipendra-bucket-4") # this will give an error because tuple is immutable
s3_bucket_list.remove("dipendra-bucket-1") # this will give an error because tuple is immutable