

#calss header
class _COMPLACENT():
	def __init__(self,): 
		self.name = "COMPLACENT"
		self.definitions = [u'feeling so satisfied with your own abilities or situation that you feel you do not need to try any harder: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
