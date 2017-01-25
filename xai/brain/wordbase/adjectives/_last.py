

#calss header
class _LAST():
	def __init__(self,): 
		self.name = "LAST"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
