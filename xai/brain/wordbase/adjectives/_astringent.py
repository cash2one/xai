

#calss header
class _ASTRINGENT():
	def __init__(self,): 
		self.name = "ASTRINGENT"
		self.definitions = [u'An astringent substance causes the skin or other tissue to tighten: ', u'Astringent remarks are clever but unkind or criticize someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
