

#calss header
class _INCIDENT():
	def __init__(self,): 
		self.name = "INCIDENT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
