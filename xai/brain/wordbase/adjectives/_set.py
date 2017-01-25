

#calss header
class _SET():
	def __init__(self,): 
		self.name = "SET"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
