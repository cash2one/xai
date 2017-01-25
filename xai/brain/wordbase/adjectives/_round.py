

#calss header
class _ROUND():
	def __init__(self,): 
		self.name = "ROUND"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
