

#calss header
class _WATERTIGHT():
	def __init__(self,): 
		self.name = "WATERTIGHT"
		self.definitions = [u'having no openings to allow water to get in: ', u'(of a theory, plan, or agreement) formed very carefully in every detail so that nothing is uncertain or in doubt: ', u'If a football team has a watertight defence, it stops an opponent from scoring a goal. : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
