

#calss header
class _REPRESENTATIVE():
	def __init__(self,): 
		self.name = "REPRESENTATIVE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
