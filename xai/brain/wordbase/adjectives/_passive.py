

#calss header
class _PASSIVE():
	def __init__(self,): 
		self.name = "PASSIVE"
		self.definitions = [u'not acting to influence or change a situation; allowing other people to be in control: ', u'The passive form of a verb is being used when the grammatical subject is the person or thing that experiences the effect of an action, rather than the person or thing that causes the effect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
