

#calss header
class _SENSITIVE():
	def __init__(self,): 
		self.name = "SENSITIVE"
		self.definitions = [u'easily upset by the things people say or do, or causing people to be upset, embarrassed, or angry: ', u'A sensitive subject, situation, etc. needs to be dealt with carefully in order to avoid upsetting people: ', u'understanding what other people need, and being helpful and kind to them: ', u'easily influenced, changed, or damaged, especially by a physical activity or effect: ', u'Sensitive equipment is able to record small changes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
