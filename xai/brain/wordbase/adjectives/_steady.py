

#calss header
class _STEADY():
	def __init__(self,): 
		self.name = "STEADY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
