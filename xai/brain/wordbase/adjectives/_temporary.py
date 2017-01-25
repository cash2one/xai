

#calss header
class _TEMPORARY():
	def __init__(self,): 
		self.name = "TEMPORARY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
