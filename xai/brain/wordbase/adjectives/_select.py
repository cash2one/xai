

#calss header
class _SELECT():
	def __init__(self,): 
		self.name = "SELECT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
