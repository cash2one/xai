

#calss header
class _COMPLEX():
	def __init__(self,): 
		self.name = "COMPLEX"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
