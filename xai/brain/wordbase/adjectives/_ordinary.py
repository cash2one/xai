

#calss header
class _ORDINARY():
	def __init__(self,): 
		self.name = "ORDINARY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
