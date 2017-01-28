

#calss header
class _TOUGH():
	def __init__(self,): 
		self.name = "TOUGH"
		self.definitions = [u'strong; not easily broken or made weaker or defeated: ', u'strong and determined: ', u'difficult to do or to deal with: ', u'Tough food is difficult to cut or eat: ', u'likely to be violent or to contain violence; not kind or pleasant: ', u'unlucky: ', u"sometimes used to show that you have no sympathy for someone's problems or difficulties: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
