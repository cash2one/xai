

#calss header
class _ARMED():
	def __init__(self,): 
		self.name = "ARMED"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
