

#calss header
class _LEFT():
	def __init__(self,): 
		self.name = "LEFT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
