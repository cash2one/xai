

#calss header
class _IMPOTENT():
	def __init__(self,): 
		self.name = "IMPOTENT"
		self.definitions = [u'not having the power or ability to change or improve a situation: ', u'If a man is impotent, he cannot have sex because his penis cannot become hard or stay hard.', u'If a man is impotent, he is unable to have children.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
