

#calss header
class _MIDDLE():
	def __init__(self,): 
		self.name = "MIDDLE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata