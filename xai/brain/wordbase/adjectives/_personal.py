

#calss header
class _PERSONAL():
	def __init__(self,): 
		self.name = "PERSONAL"
		self.definitions = [u'relating or belonging to a single or particular person rather than to a group or an organization: ', u'A personal action is one that is done by someone directly rather than getting another person to do it: ', u"private or relating to someone's private life: ", u'relating to your body or appearance: ', u"an intentionally offensive remark about someone's character or appearance: ", u'to start being rude to someone about their character or appearance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
