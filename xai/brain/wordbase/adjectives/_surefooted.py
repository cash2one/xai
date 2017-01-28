

#calss header
class _SUREFOOTED():
	def __init__(self,): 
		self.name = "SUREFOOTED"
		self.definitions = [u'able easily to walk on rough ground, without falling: ', u'showing confidence and the ability to make good judgments in a difficult situation']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
