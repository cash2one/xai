

#calss header
class _SHOOTING():
	def __init__(self,): 
		self.name = "SHOOTING"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
