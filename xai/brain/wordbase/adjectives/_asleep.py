

#calss header
class _ASLEEP():
	def __init__(self,): 
		self.name = "ASLEEP"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
