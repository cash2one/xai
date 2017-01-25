

#calss header
class _DOWN():
	def __init__(self,): 
		self.name = "DOWN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
