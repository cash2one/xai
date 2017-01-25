

#calss header
class _DEVELOPING():
	def __init__(self,): 
		self.name = "DEVELOPING"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
