

#calss header
class _HEARING():
	def __init__(self,): 
		self.name = "HEARING"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
