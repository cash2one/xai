

#calss header
class _SUFFOCATING():
	def __init__(self,): 
		self.name = "SUFFOCATING"
		self.definitions = [u'Something that is suffocating makes you feel uncomfortably hot or unable to breathe: ', u'preventing something or someone from improving or developing in a positive way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
