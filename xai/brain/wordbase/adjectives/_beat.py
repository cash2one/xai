

#calss header
class _BEAT():
	def __init__(self,): 
		self.name = "BEAT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata