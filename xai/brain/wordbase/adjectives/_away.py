

#calss header
class _AWAY():
	def __init__(self,): 
		self.name = "AWAY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
