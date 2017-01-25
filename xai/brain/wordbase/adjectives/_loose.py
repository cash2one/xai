

#calss header
class _LOOSE():
	def __init__(self,): 
		self.name = "LOOSE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
