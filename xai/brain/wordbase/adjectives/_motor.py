

#calss header
class _MOTOR():
	def __init__(self,): 
		self.name = "MOTOR"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
