

#calss header
class _IN():
	def __init__(self,): 
		self.name = "IN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
