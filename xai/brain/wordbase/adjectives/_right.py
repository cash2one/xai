

#calss header
class _RIGHT():
	def __init__(self,): 
		self.name = "RIGHT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
