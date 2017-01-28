

#calss header
class _RAPT():
	def __init__(self,): 
		self.name = "RAPT"
		self.definitions = [u'giving complete attention, or showing complete involvement, or (of attention) complete: ', u'extremely happy or excited']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
